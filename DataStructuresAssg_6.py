def renameKey(my_dict):
    value = my_dict.get("city")
    del my_dict["city"]
    my_dict.update({"location":value})
    print(my_dict)


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
renameKey(sampleDict)
