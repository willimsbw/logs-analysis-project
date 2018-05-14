CREATE OR REPLACE VIEW top_articles AS SELECT title, visits
  FROM (
    SELECT articles.title, articles.author, articles.slug, article_views.path, article_views.visits
      FROM articles, (
        SELECT path, count(*) AS visits
          FROM log
          WHERE status='200 OK'
          GROUP BY path
      ) AS article_views
      WHERE article_views.path=CONCAT('/article/', articles.slug)
  ) AS articles_info
  ORDER BY visits DESC LIMIT 3;
