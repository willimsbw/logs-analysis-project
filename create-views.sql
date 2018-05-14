CREATE OR REPLACE VIEW articles_info AS SELECT articles.title, articles.author, articles.slug, article_views.path, article_views.visits
  FROM articles, (
    SELECT path, count(*) AS visits
      FROM log
      WHERE status='200 OK'
      GROUP BY path
  ) AS article_views
  WHERE article_views.path=CONCAT('/article/', articles.slug)


CREATE OR REPLACE VIEW top_articles AS SELECT title, visits
  FROM articles_info
  ORDER BY visits DESC LIMIT 3;


CREATE OR REPLACE VIEW authors_views AS SELECT authors.name, sum(articles_info.visits) AS visits
  FROM articles_info, authors
	WHERE articles_info.author=authors.id
	GROUP BY authors.name
  ORDER BY visits DESC;

CREATE OR REPLACE VIEW many_failures AS SELECT *
  FROM (
    SELECT CAST(CAST(failed_requests.num AS DECIMAL (10,2))/CAST(all_requests.num AS DECIMAL (10,2)) AS DECIMAL (10,2)) AS percent, all_requests.time
    FROM (
      SELECT count(*) as num, time::date
        FROM log
        WHERE status!='200 OK'
        GROUP BY time::date
        ORDER BY num DESC
    ) AS failed_requests, (
      SELECT count(*) as num, time::date
        FROM log
        GROUP BY time::date
        ORDER BY num DESC
    ) AS all_requests
    WHERE failed_requests.time=all_requests.time
    ORDER BY percent DESC
    ) AS percent_failures
  WHERE percent>0.01;




  select count(*) as num, time::date
    FROM log
    WHERE status!='200 OK'
    GROUP BY time::date
    ORDER BY num DESC;


  SELECT count(*) as num, time::date
    FROM log
    GROUP BY time::date
    ORDER BY num DESC;

SELECT *
  FROM (
    SELECT CAST(CAST(failed_requests.num AS DECIMAL (10,2))/CAST(all_requests.num AS DECIMAL (10,2)) AS DECIMAL (10,2)) AS percent, all_requests.time
      FROM failed_requests, all_requests
      WHERE failed_requests.time=all_requests.time
      ORDER BY percent DESC
    ) AS foo
    WHERE percent>0.01;
