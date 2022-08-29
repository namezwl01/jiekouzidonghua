import requests

url="http://192.168.43.128/prod-api/system/role"

p={
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmMjMyNTJiLWE1NTgtNDVhOC04MThhLWJmMzg0M2UwYzU4NiJ9.NhS-0mXr0PNzEFJcTwrp_pVcZ8Xc8S_EH39XR6WwwOIfZQ9vUhrC5orQKbzsOi--BCgt-L0b_4xs15BE9QHd0w",
    "Content-Type":"application/json;charset=UTF-8"

}
s={"roleName":"12222","roleKey":"122","roleSort":0,"status":"0","menuIds":[],"deptIds":[],"menuCheckStrictly":True,"deptCheckStrictly":True}

res=requests.post(url=url,json=s,headers=p)
print(res.json())