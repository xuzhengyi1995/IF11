import pymongo
import time
from multiprocessing import pool
from multiprocessing import cpu_count
from math import radians, cos, sin, asin, sqrt
import collections
import threadpool

try:
    from Blockchain import settings
    from mongoDB.models import haversine
except:
    import settings
    from models import haversine

class Db:
    '''
    For mongodb
    time range 1201955444 to 1202488759
    '''

    def __init__(self, ssl=False):
        self.ip = settings.mongodb_ip
        self.db = settings.mongodb_db
        self.ssl = ssl
        self.client = pymongo.MongoClient(self.ip, ssl=self.ssl)

    def getDB(self, dbname=False):
        _database = self.client[self.db] if(not dbname) else _client[dbname]
        return _database

    def getCollection(self, collection):
        _db = self.getDB()
        if(not collection in _db.collection_names(include_system_collections=False)):
            raise(Exception('Do not have collection \'%s\'.' % collection))
        co = _db[collection]
        return co

def calculateDistance(car1_info, car2_info):
    """car_info {"timestamp", "id", "lat", "long"}"""
    return haversine(car1_info[0], car1_info[1], car2_info[0], car2_info[1])

def calculateDistanceForRangeTime(time_index, set_range):
    # testdb = Db()
    r = testdb.getCollection('nice_trace')
    r2 = testdb.getCollection('frag' + str(set_range))
    res = r.find_one({"time": time_index}, {"cars_info": 1})
    try:
        if res:
            cars_info = res["cars_info"]
            #{"2": [129.555, 39.5656]}
            cars_id = []
            # get res first to avoid
            for kcar in cars_info.keys():
                cars_id.append(kcar)
            varys_res = []
            # variable to stock mongoDB document to save time at insert
            list_cars_distance = {}
            for vary_time in range(time_index + 1, time_index + set_range):
                varys_res.append(r.find_one({"time": vary_time}, {"cars_info": 1}))
            for index1 in range(len(cars_id) - 1):
                for index2 in range(index1 + 1, len(cars_id)):
                    car1 = cars_id[index1]
                    car2 = cars_id[index2]
                    car1_info = [cars_info[car1]]
                    car2_info = [cars_info[car2]]
                    for vary_res in varys_res:
                        if vary_res:
                            if car1 in vary_res["cars_info"].keys():
                                car1_info.append(vary_res["cars_info"][car1])
                            if car2 in vary_res["cars_info"].keys():
                                car2_info.append(vary_res["cars_info"][car2])
                    distances = []
                    for vector1 in car1_info:
                        for vector2 in car2_info:
                            distances.append((calculateDistance(vector1, vector2)))
                    if int(car1) > int(car2):
                        list_cars_distance[car2 + ',' + car1] = min(distances)
                    else:
                        list_cars_distance[car1 + ',' + car2] = min(distances)
            r2.insert_one({"time": time_index, "list_cars_distance": list_cars_distance})
            # return {"time": time_index, "list_cars_distance": list_cars_distance}
    except Exception as e:
        print(e)

def groupTime(time_index):
    """for grouping all cars in one time"""
    testdb = Db()
    r = testdb.getCollection('trace')
    r2 = testdb.getCollection('nice_trace')
    res = r.find({"time": time_index}, {"id": 1, "longitude": 1, "latitude": 1})
    len = res.count()
    cars_info = {}
    try:
        for index in range(len):
            cars_info[str(res[index]["id"])] = [res[index]["longitude"], res[index]["latitude"]]
        r2.insert_one({"time": int(time_index), "cars_info": cars_info})
    except Exception as e:
        print(e)

def insertCarsDistance(info_dictionary):
    try:
        r3.insert_one(info_dictionary)
    except:
        pass

def threadWorker(begin, end, set_range):
    thread = threadpool.ThreadPool(num_workers=10)
    var_list = [([i, set_range], None) for i in range(begin, end)]
    requests = threadpool.makeRequests(calculateDistanceForRangeTime, var_list)
    [thread.putRequest(req) for req in requests]
    thread.wait()

def init_processes():
    global testdb
    testdb = Db()

def makeContactInDb(time_range):
    start = time.time()
    pool1 = pool.Pool(processes=5, initializer=init_processes)
    set_range = time_range
    st = int((1202488761 - 1201955444)/30)
    begin = 0
    end = 1201955444
    for i in range(0, 31):
        # 1201955444, 1202488760
        begin = end
        end = begin + st if(begin+st<1202488761) else 1202488761
        print(begin,end)
        result = pool1.apply_async(threadWorker, (begin, end, set_range,))
    pool1.close()
    pool1.join()
    if result.successful():
        print("good execution")
    end = time.time()
    print("make time for " + time_range + " in " + end - start)

if __name__ == '__main__':
    pass
    # testdb = Db()
    # r = testdb.getCollection('trace')
    # k = r.find({}, {"time": 1, "_id": 0})
    # k2 = r.find({"time": {"$gt": 1}}, {"time": 1, "_id": 0})
    # r.remove({"id": 1})
    # r.insert_one({"id": 1, "time": 1201962968.0, "long": 116.51172, "lag": 39.92123})
    # print(r)
