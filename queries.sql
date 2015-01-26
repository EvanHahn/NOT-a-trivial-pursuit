select count(*) from Players where gender = 'female';

select count(*) from Players where gender = 'male';

select count(*) from Players;

select s.gameid from scores s
join players p1, p2, p3
where p1.id < p2.id
and p1.id < p3.id
and p2.id < p3.id
and p1.gender = 'female'
and p2.gender = 'female'
and p3.gender = 'female'
and s.playerid = p1.id and s.playerid = p2.id and s.playerid = p3.id


select count(*) g.gameid from games G 
join scores S on G.gameid = S.gameid
