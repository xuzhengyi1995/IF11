from dejavu.stroge import db_class

if __name__ == '__main__':
    dbe = db_class("LevelDB")
    db = dbe("fingerPrints", True)
    i = db.iterator()
    #db.put(b"abccc",b"121|321435")
    with db.iterator() as it:
        for k, v in it:
            print(k, v)
    it.close()
    db.close()
