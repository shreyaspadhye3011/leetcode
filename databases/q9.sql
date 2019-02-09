CREATE VIEW AL_PACINO_VIEW AS
SELECT ACTOR, COUNT(ACTOR) AS AL_COUNT 
FROM MOVIE_ACTOR_LIST 
WHERE MID IN (SELECT DISTINCT(MID) FROM MOVIE_ACTOR_LIST WHERE ACTOR='P6') 
GROUP BY ACTOR;


SELECT NAME 
FROM PERSON 
WHERE PID IN (SELECT ACTOR FROM AL_PACINO_VIEW WHERE AL_COUNT = (SELECT MAX(AL_COUNT) FROM AL_PACINO_VIEW));