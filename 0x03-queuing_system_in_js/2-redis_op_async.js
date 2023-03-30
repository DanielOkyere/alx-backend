/**
 * 1-redis_op.js file
 */
import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
    console.log("Redis client not connected to the server:", err.toString()),
);
client.on("connect", async () => {
    console.log('Redis client connect to the server');
    await main();
});

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
    console.log(await promisify(client.GET).bind(client)(schoolName));
}

async function main() {
    await displaySchoolValue("Holberton");
    setNewSchool("HolbertonSanFrancisco", "100");
    await displaySchoolValue("HolbertonSanFrancisco");
}
