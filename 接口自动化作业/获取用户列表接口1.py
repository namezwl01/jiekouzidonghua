import requests


url="http://192.168.43.128/prod-api/system/user/list"

p = {
    "Content-Type":"application/json",
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmMjMyNTJiLWE1NTgtNDVhOC04MThhLWJmMzg0M2UwYzU4NiJ9.NhS-0mXr0PNzEFJcTwrp_pVcZ8Xc8S_EH39XR6WwwOIfZQ9vUhrC5orQKbzsOi--BCgt-L0b_4xs15BE9QHd0w",
    "Cookie":"username=admin; rememberMe=true; password=Z2yRS3QeY7k5KzpZ4JcgnLK6QKCG+NvhX9j3GAh3MLEXo8HmC95/JQEqTWL7joV7yxTWbpDV70JGRxemvXM3iA==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjZmMjMyNTJiLWE1NTgtNDVhOC04MThhLWJmMzg0M2UwYzU4NiJ9.NhS-0mXr0PNzEFJcTwrp_pVcZ8Xc8S_EH39XR6WwwOIfZQ9vUhrC5orQKbzsOi--BCgt-L0b_4xs15BE9QHd0w"
}

res=requests.get(url=url,headers=p)

print(res.text)