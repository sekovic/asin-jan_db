from fastapi import FastAPI
from pydantic import BaseModel
from SPAPI import getDictFromAPI,extractData
from database.ItemsData import put_new_no, put_items,test_db

class Item(BaseModel):
    user_id: str
    code_type: str
    refresh_token: str
    codes: str

app = FastAPI()

@app.post("/item/")
async def get_items(item: Item):
    user_id=item.user_id
    code_type=item.code_type
    refresh_token = item.refresh_token
    input_codes_str=item.codes

    res=getDictFromAPI(code_type,input_codes_str, refresh_token)
    data_dict=extractData(res)    

    
    split_codes(user_id, code_type, refresh_token, input_codes_str)

    return "InProgress"
#    return data_dict
#    test=test_db()
#    return test

@app.get("/item/")
async def get_items(user_id: str, code_type: str, refresh_token: str, codes: str):

    res=getDictFromAPI(code_type,codes, refresh_token)
    data_dict=extractData(res)    
    #split_codes(user_id, code_type, refresh_token, codes)

#    return "InProgress"

    return data_dict
    


def split_codes(user_id: str, code_type: str, refresh_token: str, codes: str):
    codes_list=codes.split(',')

    #配列の要素数をカウント
    length = len(codes_list)
    
    #開始位置を指定
    n = 0
    
    #分割する変数の個数を指定
    s = 10

    #配列を指定した個数で分割していくループ処理
    for i in codes_list:
        #print(codes_list[n:n+s:1])

        no=put_new_no(user_id)
        #no=1
#        print("no=" + str(no))

        new_codes_list=codes_list[n:n+s:1]
        new_codes=','.join(new_codes_list)
        print("new_codes:"+new_codes)
        res=getDictFromAPI(code_type,new_codes, refresh_token)
        data_dict=extractData(res)
        print(data_dict)
        put_items(no, data_dict)

        n += s
    
        #カウント数が配列の長さを超えたらループ終了
        if n >= length:
            break

 


if __name__ == '__main__':
    main()