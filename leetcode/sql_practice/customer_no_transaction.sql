# Write your MySQL query statement below
# Table: Visits

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | visit_id    | int     |
# | customer_id | int     |
# +-------------+---------+
# visit_id is the column with unique values for this table.
# This table contains information about the customers who visited the mall.
 

# Table: Transactions

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | transaction_id | int     |
# | visit_id       | int     |
# | amount         | int     |
# +----------------+---------+
# transaction_id is column with unique values for this table.
# This table contains information about the transactions made during the visit_id.
 

# Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

# Return the result table sorted in any order.


select v.customer_id, COUNT(v.visit_id) as count_no_trans
from visits v
left join transactions t on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id
