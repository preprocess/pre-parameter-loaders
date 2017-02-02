--DESCRIPTION--

Test parameter loader macros

--GIVEN--

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

--EXPECT--

class Fixture
{
    public function typeHintedRegular(string $string ="typeHintedRegular")
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

    public function multipleRegular($one ="one", $two =2.2, $three =true, $four =null)
    {
        return "working";
    }

    public function multipleEnhanced($one = null, $two = null)
    {
        if (is_null($one)) {
            $one =  ucwords("one");
        }

        if (is_null($two)) {
            $two =  round(2.2);
        }

        return "working";
    }

    public function mixed($one, $two =2.2, $three = null, $four = null)
    {
        if (is_null($three)) {
            $three =  round(3.3);
        }

        if (is_null($four)) {
            $four = new stdClass ;
        }

        return "working";
    }
}
