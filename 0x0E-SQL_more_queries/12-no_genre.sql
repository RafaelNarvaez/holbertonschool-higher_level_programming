-- script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON show_id = id
WHERE tv_show_genres.GENRE_ID IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;