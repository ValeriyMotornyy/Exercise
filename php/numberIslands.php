<?php

function main()
{
    // Islands array
    $islands = [
        [1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
    ];

    // Calculating number rows and columns
    $rows    = count($islands);
    $columns = count($islands[0]);
    $count   = 0;

    // Array of possitions to check
    $positions = function($i, $j) use ($columns, $rows) {
        return [
            [$j != $columns - 1, $i, $j + 1], // Next
            [$j != 0,            $i, $j - 1], // Prev
            [$i != 0,            $i - 1, $j], // Above
            [$i != $rows - 1,    $i + 1, $j], // Below
        ];
    };

    // Iterate each row
    for ($i = 0; $i < $rows; $i++) {

        // Iterate each column
        for ($j = 0; $j < $columns; $j++) {

            // Check for islands
            if ($islands[$i][$j] == 1) {

                // Checking adjacent possitions to find a required value
                foreach ($positions($i, $j) as $key) {
                    if ($key[0] && $islands[$key[1]][$key[2]] == 1) {

                      // If adjacent value found increment count and reset found value (to mark as found)
                      $count++;
                      $islands[$key[1]][$key[2]] = 0;
                      var_dump("x-axis: {$j} -- y-axis: {$i}");
                    }
                }
                $islands[$i][$j] = 0;
            }
        }
    }
    var_dump($count);
}
main();
