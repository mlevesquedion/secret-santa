# Secret Santa

Inspired by [this](http://blog.vmchale.com/article/secret-santa) blog post.

## Problem

Devise an algorithm to randomly assign coworkers to get each other gifts. A worker should not be assigned to himself.

## Solution

Shuffle the workers once, requiring O(n) time. Then simply pair up each worker with the next one in the permutation, wrapping around at the end.
