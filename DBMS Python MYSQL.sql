Use Amdocs_system ;







#5- Transaction according to date

select transaction_date,amount from transaction 
where account_number=1 and
day(transaction_date)=28 and year(transaction_date)=2023;

#6- top 5 highest balance_amt customers

select bk.Account_Number,cust.Name,bk.total_balance from customers as cust
join balance as bk on
bk.Account_Number=cust.Account_Number
order by bk.total_balance DESC
LIMIT 5;

#7- count total number of transactions per customer by date

select account_number,count(*)  as t_count
from transaction 
where transaction_date="2023-08-28"
group by account_number;


#8- count total number of transactions per customer by month

select account_number,count(*)  as t_count
from transaction 
where month(transaction_date)=8
group by account_number;

#9- count total number of transactions per customer from certain date

select account_number,count(*)  as t_count
from transaction 
where transaction_date between "2023-01-01" and curdate()
group by account_number;

#10- 8 display customers details having < 5000 balance amount

select account_number, total_balance
from balance
where total_balance < 5000;

#11- display customers details who has city "pune"

select * from customers
where address = "Pune";

#12- display no of transactions in a day city wise 

select c.address, count(*) as trans_count
from customers as c
join transaction as t
on c.account_number=t.account_number
where c.address="Pune";

#13- display the customer details whoes maximum bank balance amount in city wise

select name,total_balance 
from customers as cust
join balance as bk
where cust.address = 'Pune'
order by bk.total_balance desc
limit 1;

#14- display the customers details whose birthday is today

select * from customers 
where DOB=curdate();

#15- display the customers details who having max transaction in a week

select c.name, t.transaction_date
from customers as c
join transaction as t
where t.transaction_date between '2023-08-20' and '2023-08-28';


#16- display the customers details who having max transaction in a month

select c.account_number, c.name, 
month(t.transaction_date), max(t.amount) as max_trans_amt
from customers c
join transaction t on c.account_number = t.account_number
where month(t.transaction_date) = 8 and year(t.transaction_date) = 2023
group by c.account_number, c.name,month(t.transaction_date)
having max_trans_amt = (select max(amount)
					from transaction
					where month(transaction_date) = 8 and year(transaction_date) = 2023);

