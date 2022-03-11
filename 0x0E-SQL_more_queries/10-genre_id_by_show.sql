-- script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked
Select tv_shows.title, tv_show_genres.genre_id From tv_shows
Inner Join tv_shows_genres On tv_shows.id = tv_show_genres.show_id
Order By tv_shows.title, tv_show_genres.genre_id;
