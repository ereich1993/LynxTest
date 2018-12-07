
select gender, avg(duration) as duration from calls join customers on calls.callee_id = customers.id
group by  gender;



