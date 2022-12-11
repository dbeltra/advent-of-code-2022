from dataclasses import dataclass, field
import operator

ops = { '+' : operator.add, '*' : operator.mul}

with open("input.txt") as f:
    data = f.read().splitlines()

@dataclass
class Monkey():
    id: int = 0
    items: list = field(default_factory=list)
    operation_symbol: str = "+"
    operation_operator_1: str = '1'
    operation_operator_2: str = '1'
    test: int = 0
    true_target_id: int = 0
    false_target_id: int = 0
    items_inspected_count: int = 0

    def play_round(self, decreasing_worry=True):
        for item in self.items:
            self.items_inspected_count += 1
            o1 = self.operation_operator_1
            if self.operation_operator_1 == 'old':
                o1 = item
            o2 = self.operation_operator_2
            if self.operation_operator_2 == 'old':
                o2 = item
            new_worry = ops[self.operation_symbol](int(o1), int(o2))
            if decreasing_worry:
                new_worry = int(new_worry / 3)
            else:
                pass
            if new_worry % self.test == 0:
                monkey_list[self.true_target_id].items.append(new_worry)
            else:
                monkey_list[self.false_target_id].items.append(new_worry)
        self.items = []

def parse_input(data):
    monkey_list = []
    monkey = Monkey()
    for line in data:
        if line.startswith('Monkey'):
            monkey_id = line.split('Monkey ')[1].split(':')[0]
            monkey.id = int(monkey_id)
        if 'Starting items' in line:
            items = line.split('Starting items: ')[1].split(',')
            for i in items:
                monkey.items.append(int(i))
        if 'Operation' in line:
            o1, symbol, o2 = line.split('new = ')[1].split(' ')
            monkey.operation_operator_1 = o1
            monkey.operation_operator_2 = o2
            monkey.operation_symbol = symbol

        if 'Test' in line:
            monkey.test = int(line.split('divisible by ')[1])
        if 'If true' in line:
            monkey.true_target_id = int(line.split('monkey ')[1])
        if 'If false' in line:
            monkey.false_target_id = int(line.split('monkey ')[1])
            monkey_list.append(monkey)
            monkey = Monkey()

    return monkey_list


def get_monkey_business():
    m = sorted(monkey_list, key=lambda x : x.items_inspected_count, reverse=True)
    return m[0].items_inspected_count * m[1].items_inspected_count

monkey_list = parse_input(data)
for cur_round in range(20):
    for monkey in monkey_list:
        monkey.play_round()

mb1 = get_monkey_business()
print(f'Solution to part one {mb1}')
