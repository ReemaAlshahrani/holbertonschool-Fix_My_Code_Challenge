#!/usr/bin/node
/**
 * Prints a square of a given size using the character '#'
 */

const args = process.argv.slice(2);

if (args.length > 0) {
    const size = parseInt(args[0], 10);

    if (isNaN(size) || size <= 0) {
        // Do nothing or exit if size is invalid or zero/negative
    } else {
        for (let i = 0; i < size; i++) {
            console.log('#'.repeat(size));
        }
    }
}
