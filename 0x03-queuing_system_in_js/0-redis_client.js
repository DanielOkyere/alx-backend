/**
 * Redis server client
 *
 */
import { createClient } from 'redis';
async function connectRedis(){
	const client = createClient();
	client.on('error', err => console.log('Redis Client Error', err));
	await client.connect();

	await client.set('key', 'value');
	const value = await client.get('key');
	await client.disconnect();
}

const data = connectRedis();
