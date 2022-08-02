-- Dense rank window solution
select max(a.salary) as SecondHighestSalary from 
(select salary, dense_rank() over (order by salary desc) as rn
from Employee) a
where a.rn = 2

-- Max solution
select max(Salary) AS SecondHighestSalary from Employee
where salary < (Select Max(Salary) from Employee);