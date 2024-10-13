select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      -- tests/select_all.sql

select * from "Telegram_data"."public"."select_all"
where message_text is null
      
    ) dbt_internal_test