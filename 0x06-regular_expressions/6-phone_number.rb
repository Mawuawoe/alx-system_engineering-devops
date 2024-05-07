#!/usr/bin/env ruby
# A regexp that is matches 10 digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
