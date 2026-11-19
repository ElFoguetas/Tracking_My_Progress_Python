# La funcion join nos permite unir listas en una sola variable en forma de texto
letters = ["p", "y", "t", "h", "o", "n"]

url_path = "/".join(["mysite.com", "products", "sale"])
date_format = "-".join(["2026", "05", "29"]) 
crowd = " ".join(["hip", "hip", "hooray"]) 
text = "".join(letters) 

print(letters)
print(url_path)
print(date_format)
print(crowd)
print(text)