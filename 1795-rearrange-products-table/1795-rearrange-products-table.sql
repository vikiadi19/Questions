# Write your MySQL query statement below
SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' AS store, store2 AS price from Products where store2 is not null
union 
select product_id, 'store3' as store, store3 AS price from Products where store3 is not null

order by 1, 2 asc