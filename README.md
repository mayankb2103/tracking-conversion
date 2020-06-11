# tracking-conversion
```
python3 track-conversion.py
```
If you feel that json generated is two big, remove the indent parameter
From 

```
with open("name.json","w") as f:
    json.dump(resdct,f,indent=4)
```

 to 

```
with open("name.json","w") as f:
    json.dump(resdct,f)
```
