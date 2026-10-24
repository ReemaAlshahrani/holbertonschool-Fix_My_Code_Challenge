#!/usr/bin/ruby
# Collect all arguments, convert them to integers, sort them numerically, and print each one

numbers = ARGV.map { |arg| arg.to_i }
numbers.sort.each do |num|
  puts num
end
