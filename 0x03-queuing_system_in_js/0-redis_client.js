/**
 * Redis server client
 *
 */
import { createClient } from 'redis';
async function connectRedis(){
	const client = createClient();
	client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));
	client.on('connect', () => console.log('Redis client connected to the server'));
}

const data = connectRedis();
