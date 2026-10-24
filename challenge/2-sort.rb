#!/usr/bin/ruby
# Collect only valid integer arguments, sort them numerically, and print each one

numbers = ARGV.map { |arg| Integer(arg) rescue nil }.compact
numbers.sort.each do |num|
  puts num
end
