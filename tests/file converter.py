import ss,glob

for file in glob.glob("*.ss"):
    with open(file) as f:
        data = ss.load(f)
    with open(str(file.split(".")[0])+".SHIVAM",'w') as x:
        ss.dump(data,x)

print(data,file.split(".")[0])
