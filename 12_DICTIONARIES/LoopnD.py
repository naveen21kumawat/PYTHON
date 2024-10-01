myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : {
       "dob" : 1978,
       "dod" : 2023
    }
  }
}

print(myfamily)

for child, obj in myfamily.items():
    print(child)

    for key, value in obj.items():
      if isinstance(value,dict):
         print(f"   {key}:")
         for k, v in value.items():
            print(f"    {k} : {v}")
      else:
        print(f"    {key} : {value}")

# print(myfamily["child1"]["name"])

# del myfamily["child1"]["year"]
# print(myfamily)


