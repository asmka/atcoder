# frozen_string_literal: true

module Direction
  EAST = 'EAST'
  SOUTH = 'SOUTH'
  WEST = 'WEST'
  NORTH = 'NORTH'
end

def main
  _n = gets.chomp
  t = gets.chomp

  dir = Direction::EAST
  pos = { x: 0, y: 0 }
  t.each_char do |c|
    case c
    when 'S'
      pos = move(pos, dir)
    when 'R'
      dir = rotate(dir)
    end
  end

  print(pos[:x], ' ', pos[:y])
end

def move(pos, dir)
  case dir
  when Direction::EAST
    { x: pos[:x] + 1, y: pos[:y] }
  when Direction::SOUTH
    { x: pos[:x], y: pos[:y] - 1 }
  when Direction::WEST
    { x: pos[:x] - 1, y: pos[:y] }
  when Direction::NORTH
    { x: pos[:x], y: pos[:y] + 1 }
  end
end

def rotate(dir)
  case dir
  when Direction::EAST
    Direction::SOUTH
  when Direction::SOUTH
    Direction::WEST
  when Direction::WEST
    Direction::NORTH
  when Direction::NORTH
    Direction::EAST
  end
end

main
