class Fixture
{
    public function typeHintedRegular(string $string = "typeHintedRegular")
    {
        return "working";
    }

    public function typeHintedEnhanced(stdClass $object = new stdClass())
    {
        return "working";
    }

    public function multipleRegular($one = "one", $two = 2.2, $three = true, $four = null)
    {
        return "working";
    }

    public function multipleEnhanced($one = ucwords("one"), $two = round(2.2))
    {
        return "working";
    }

    public function mixed($one, $two = 2.2, $three = round(3.3), $four = new stdClass)
    {
        return "working";
    }
}

~~~

class Fixture
{
    public function typeHintedRegular(string $string = "typeHintedRegular")
    {
        return "working";
    }

    public function typeHintedEnhanced(stdClass $object = null)
    {
        if (is_null($object)) {
            $object = new stdClass();
        }

        return "working";
    }

    public function multipleRegular(
        $one = "one",
        $two = 2.2,
        $three = true,
        $four = null
    ) {
        return "working";
    }

    public function multipleEnhanced($one = null, $two = null)
    {
        if (is_null($one)) {
            $one = ucwords("one");
        }
        if (is_null($two)) {
            $two = round(2.2);
        }

        return "working";
    }

    public function mixed($one, $two = 2.2, $three = null, $four = null)
    {
        if (is_null($three)) {
            $three = round(3.3);
        }
        if (is_null($four)) {
            $four = new stdClass();
        }

        return "working";
    }
}

---

$anon = function($a = true, $b = "hello", $c = ucwords("world")) {
    print $b . " " . $c;
};

~~~

$anon = function ($a = true, $b = "hello", $c = null) {
    if (is_null($c)) {
        $c = ucwords("world");
    }

    print $b . " " . $c;
};

---

$anon = function($driver = new Driver("hello world", 12)) {
    return $driver->fn();
};

~~~

$anon = function ($driver = null) {
    if (is_null($driver)) {
        $driver = new Driver("hello world", 12);
    }

    return $driver->fn();
};
