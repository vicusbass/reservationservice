import http from 'k6/http';
import { check } from 'k6';

const url = 'http://192.168.1.13:8002/reservations';

function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

export default function() {
    const payload = {
        'restaurant_id': randomInt(1, 100),
        'table_id': randomInt(1, 20),
        'start': '2020-06-24 20:05:44',
        'end': '2020-06-24 20:06:44',
        'guests': randomInt(1,6)
    }
    let result = http.post(url, JSON.stringify(payload));
    check(result, {
        'is status 201': (r) => r.status === 201,
    });
}