SELECT user_id, reaction AS dominant_reaction, ROUND(count_reaction/count_all_reaction,2) AS reaction_ratio 
FROM (
    SELECT DISTINCT
        user_id, reaction, 
        COUNT(*) OVER (PARTITION BY user_id, reaction) AS count_reaction, 
        COUNT(*) OVER (PARTITION BY user_id) AS count_all_reaction
    FROM reactions
)AS t
WHERE count_all_reaction>=5 AND count_reaction/count_all_reaction>=0.6
ORDER BY reaction_ratio DESC, user_id 