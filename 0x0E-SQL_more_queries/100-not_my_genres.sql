-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT tv_genres.id
    FROM tv_genres
    JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS dexter_genres ON tv_genres.id = dexter_genres.id
WHERE dexter_genres.id IS NULL
ORDER BY tv_genres.name ASC;
