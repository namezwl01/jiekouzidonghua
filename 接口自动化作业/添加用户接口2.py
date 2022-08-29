import requests
url="http://192.168.43.128/prod-api/system/user"
p={
    "Content-Type":"application/json;charset=UTF-8",
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmMjMyNTJiLWE1NTgtNDVhOC04MThhLWJmMzg0M2UwYzU4NiJ9.NhS-0mXr0PNzEFJcTwrp_pVcZ8Xc8S_EH39XR6WwwOIfZQ9vUhrC5orQKbzsOi--BCgt-L0b_4xs15BE9QHd0w",

}
ji={"userName":"2222","nickName":"2222","password":"123456","status":"0","postIds":[],"roleIds":[]}
jes=requests.post(url=url,json=ji,headers=p)
print(jes.json)

