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
def put_items(no, items):
    items_db.put({"no":no,"items":items})



def put_new_no(user_id):
    print("put_new_no:"+user_id)
    no=get_maxno_by_userid(user_id)
    #print(no)
    d=datetime.datetime.now()
    print(d.strftime('%Y/%m/%d %H:%M:%S'))
    dataset_db.put({"no":no,"user_id":user_id,"date_reg":d.strftime('%Y/%m/%d %H:%M:%S'),"state":0})
    return no

def get_maxno_by_userid(user_id):
    print("get_maxno_by_userid")
    try:
        res = dataset_db.fetch({"user_id":user_id})
    except:
        print("error: dataset_db.fetch")
        return 1
    
    print("all_items")
    if not res is None:
        all_items = res.items
        try:
            print("try")
            max_item=max(all_items, key=lambda x: x["no"])
            return max_item['no']+1
            print ("max_item['no']:"+max_item['no'])
        except ValueError:
            print("000")
            return 1
    #return max_item['no']
    else:
        return 1

        
'''
def putData(items,)
db.put(key[key],datetime.datetime.now())
print(f"kei={key}")
'''


def test_db():
    return 'test_db'

def main():
    items=None
    put_items("a",items)

if __name__ == "__main__": 
    main()