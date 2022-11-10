from deta import Deta  # Import Deta
import datetime

# Initialize with a Project Key
deta = Deta("c0j0yuic_Gm7mjVA9U149xt8KRyLrfJwsiDyxbPXS")

#def get_maxno_dataset_by_user(user_id)

# This how to connect to or create a database.
dataset_db = deta.Base("dataset_db")
items_db = deta.Base("items_db")

'''
db.put({"no":1,"user_id":"a","date_reg":"2022/11/1","state":"1"})
db.put({"no":2,"user_id":"b","date_reg":"2022/11/2","state":"1"})
db.put({"no":3,"user_id":"c","date_reg":"2022/11/3","state":"1"})
db.put({"no":4,"user_id":"D","date_reg":"2022/11/4","state":"1"})
'''
def test_fetch(key):
    res = dataset_db.fetch({"user_id": key})
    all_items = res.items
    print("#(test) all_items:"+str(all_items))
    #return all_items

def test_no_put(key):
    test_fetch(key)


def put_new_no(user_id: str):

    no=get_maxno_by_userid(user_id)
    d=datetime.datetime.now()
    print(d.strftime('%Y/%m/%d %H:%M:%S'))
    dataset_db.put({"no":no,"user_id":user_id,"date_reg":d.strftime('%Y/%m/%d %H:%M:%S'),"state":0})
    return no

def get_maxno_by_userid(user_id: str):

    test_no_put(user_id)
    
    
    try:
#        res = dataset_db.fetch({"user_id":str(user_id)})
#        res = dataset_db.fetch({"user_id": "a"})
        res = dataset_db.fetch({"user_id": user_id})
#        all_items=test_no_put(user_id)
        print("success:dataset_db.fetch user_id:"+user_id)
    except:
        print("error: dataset_db.fetch user_id;"+user_id)
        return 1

    if not res is None:
        try:
            all_items = res.items
            print("all_items:"+str(all_items))
        except:
            print("all_items = res.items error:")
            return 100
        
        try:
            print("try")
            max_item = max(all_items, key=lambda x: x['no'])
            print("max_item:"+ str(max_item))
            print ("max_item['no']:"+str(max_item['no']))
            return int(max_item['no'])+1
        except ValueError:
            print("000")
            return 1
    #return max_item['no']
    else:
        return 1

def put_items(no, items_):
    items_db.put({"no":no,"items":items_})

        
'''
def putData(items,)
db.put(key[key],datetime.datetime.now())
print(f"kei={key}")
'''


def test_db():
    return 'test_db'

def main():
#    items=None
    print("a")

if __name__ == "__main__": 
    main()