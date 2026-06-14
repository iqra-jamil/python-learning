import re

text="boleh di kirim ke email saya ekoprasetyo.crb@outlook.com tks... boleh minta kirim ke db.maulana@gmail.com. dee. wien@yahoo.com. .deninainggolan@yahoo.co.id Senior Quantity Surveyor Fajar.rohita@hotmail.com, terimakasih bu Cindy Hartanto firmansyah1404@gmail.com saya mau dong bu cindy fransiscajw@gmail.com Hi Cindy ...pls share the Salary guide to donny_tri_wardono@yahoo.co.id thank a"

result=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)

print(result)


