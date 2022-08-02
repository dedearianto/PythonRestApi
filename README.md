# PythonRestApi
Demo CRUD Pyhon API with flask

# Simple flow
1. create image
2. create product
3. create variant

# How to run
1. please check mysql service, make user the service is running
2. created DB name in mysql, default database name is dbpython

  >app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/dbpython"
  

3. I used pycharm IDE, open terminal then run py app.py
![image](https://user-images.githubusercontent.com/60029017/182422294-dbfb86f3-5299-4130-b2ac-0f9ba9a1cbe7.png)

4.Test API with
  **use curl**
  
![image](https://user-images.githubusercontent.com/60029017/182422769-c0154723-fbac-4ccd-bd8a-bc52a719a6e2.png)


5. Test api with **postman**

  ![image](https://user-images.githubusercontent.com/60029017/182424103-cef85689-8e72-4e28-8098-db1f64371b7f.png)


   ***
   * URL
   ***
   # Product 
   
   CreateProduct
   
   type : POST
   
   url:http://127.0.0.1:5000/product/Baju9
   
   Body:    
   {
    "description":"the good product",
    "logo_id":1    
    } 
    
    ![image](https://user-images.githubusercontent.com/60029017/182425222-333bff01-69fd-40cd-b52c-61866cbb94f7.png)

    
    
   *** 
    UpdateProduct
    
      type : PUT
   
      url:http://127.0.0.1:5000/product/Baju9
      
      Body
      {
    "description":"the good product baju tujuh",
    "logo_id":2
      }
      
    ![image](https://user-images.githubusercontent.com/60029017/182425613-22bd4ced-5f76-46ce-8013-30aaec12b72c.png)

     
    
   *** 
   GetProduct
   
      type : GET
   
      url:http://127.0.0.1:5000/product/Baju9
   
   ![image](https://user-images.githubusercontent.com/60029017/182425936-f1e49190-3700-4c2f-8996-3d918aadffd1.png)
  
  ***    
  
  ProductList
  
  type: GET
  url: http://127.0.0.1:5000/products
  
  ![image](https://user-images.githubusercontent.com/60029017/182426318-e5c31fc0-a169-48ac-9679-435383750f84.png)

  ***
  # Variants
  ***
  Create variant
  
  type: POST
  
  url: http://127.0.0.1:5000/variant/variant1
  
  body:
  
  {
    "size":"XXXXL",
    "color":"red",
    "product_id":1
}

![image](https://user-images.githubusercontent.com/60029017/182426894-cc70daa7-b011-43f1-b379-f92c159baaae.png)

***
FindVariant

type: GET
URL : http://127.0.0.1:5000/variant/variant1


![image](https://user-images.githubusercontent.com/60029017/182427144-d162b050-1dcd-4b11-a02b-cf5c983c12d3.png)

***
VariantsList

type: GET
url: http://127.0.0.1:5000/variants

![image](https://user-images.githubusercontent.com/60029017/182427324-2c6a51ff-6a7d-49a7-81eb-54ea110f8c5b.png)

***
# Image
***
CreateImage

type : POST

url : http://127.0.0.1:5000/image

body:
{
    "url":"/home/linux/gambar/python.jpg"
}

![image](https://user-images.githubusercontent.com/60029017/182427889-b9a8f647-e0eb-424a-9a74-f283f33ffdf6.png)

***
ImageList

type: GET
url : http://127.0.0.1:5000/images

![image](https://user-images.githubusercontent.com/60029017/182428055-0fda9f47-7814-461f-89ef-a17303bf78ba.png)






  
