# bot_speaker
bot speaker lesson 3 dvmn course

to run docker
docker run -d --env-file .env --mount type=bind,source="$(pwd)"/,target=/app flashkir/bot-speaker-tm

docker run -d --env-file .env --mount type=bind,source="$(pwd)"/,target=/app flashkir/bot-speaker-vk