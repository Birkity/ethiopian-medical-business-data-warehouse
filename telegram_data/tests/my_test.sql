-- tests/select_all.sql

select * from {{ ref('select_all') }}
where message_text is null
