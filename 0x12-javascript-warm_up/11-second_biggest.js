#!/usr/bin/node

#!/usr/bin/node

const arg = process.argv[2];

function factorial(num)
{
	if (num > 0)
	{
		return (num * factorial((num - 1)));
	}
	else
	{
		return (1);
	}
}

if (Number.isInteger(Number(arg))) {
	console.log(`${factorial(parseInt(arg))}`);
      } else {
	console.log(`${1}`);
      }

