
  create view "Telegram_data"."public"."telegram_summary__dbt_tmp"
    
    
  as (
    WITH transformed_data AS (
    SELECT * FROM "Telegram_data"."public"."select_all"
)

SELECT
    channel_name,
    COUNT(message_id) AS total_messages,
    MAX(timestamp) AS latest_message
FROM transformed_data
GROUP BY channel_name
  );