### вывод команд для vault
vault secrets enable pki  
vault secrets tune -max-lease-ttl=87600h pki  
vault write -field=certificate pki/root/generate/internal         common_name="intech-global.com"         ttl=87600h > CA_cert.crt  
vault write pki/config/urls         issuing_certificates="$VAULT_ADDR/v1/pki/ca"         crl_distribution_points="$VAULT_ADDR/v1/pki/crl"  
vault secrets enable -path=pki_int pki  
vault secrets tune -max-lease-ttl=43800h pki_int  
vault write -format=json pki_int/intermediate/generate/internal         common_name="intech-global.com Intermediate Authority"         | jq -r '.data.csr' > pki_intermediate.csr  
vault write -format=json pki/root/sign-intermediate csr=@pki_intermediate.csr         format=pem_bundle ttl="43800h"         | jq -r '.data.certificate' > intermediate.cert.pem  
vault write pki_int/intermediate/set-signed certificate=@intermediate.cert.pem   
vault write pki_int/roles/example-dot-com         allowed_domains="intech-global.com"         allow_subdomains=true         max_ttl="720h"  
vault write pki_int/issue/example-dot-com common_name="netology.intech-global.com" ttl="24h" > tmp.crt  
### *.conf nginx
vagrant@ubuntu2004:~$ cat /etc/nginx/conf.d/netdate_https.conf  
server {  
    listen              80;  
    listen              443 ssl;  
    server_name         netology.intech-global.com;  
    charset             utf-8;  

        ssl_certificate            /etc/ssl/private/skynet.pem;
        ssl_certificate_key        /etc/ssl/private/skynet.key;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE


        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

    location / {
        proxy_pass              http://127.0.0.1:19999/;
        proxy_set_header        Host              $host;
        proxy_set_header        X-Real-IP         $remote_addr;
        proxy_set_header        X-Forwarded-For   $proxy_add_x_forwarded_for;
    }
}
### /etc/host
vagrant@ubuntu2004:~$ cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	ubuntu2004.localdomain

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

127.0.0.1 ubuntu2004.localdomain
127.0.0.1 netology.intech-global.com
### Вывод команды

vagrant@ubuntu2004:~$ curl https://netology.intech-global.com | head -n10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html>
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->
<html lang="en">
<head>
    <title>netdata dashboard</title>
    <meta name="application-name" content="netdata">

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
И так далее.

P.S. сильно не обисудьте, но тестировал сертификаты для ldap . совмещал учебу с работой)