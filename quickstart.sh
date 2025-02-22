docker build -t litepolis/api api/

docker network create litepolis-net

docker run -p 9030:9030 -p 8030:8030 -p 8040:8040 -itd \
                                   --net litepolis-net \
                                   --name quickstart starrocks/allin1-ubuntu

until [ "`docker inspect -f {{.State.Running}} quickstart`"=="true" ]; do
    sleep 3;
done;

docker exec -i quickstart \
            mysql -P 9030 \
            -h 127.0.0.1 -u root \
            --prompt="StarRocks > " < db.sql

docker run --net litepolis-net --name api -d -p 8000:8000 \
                              -e SQLUSER="root" \
                              -e SQLPASS="" \
                              -e SQLHOST=quickstart \
                              -e API_KEY="e54d4431-5dab-474e-b71a-0db1fcb9e659" \
                              litepolis/api
