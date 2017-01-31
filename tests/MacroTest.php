<?php

namespace Pre\ParameterLoaders;

use PHPUnit\Framework\TestCase;

class MacroTest extends TestCase
{
    public function testTypeHintedRegular()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEquals("working", $fixture->typeHintedRegular());
    }

    public function testTypeHintedEnhanced()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEquals("working", $fixture->typeHintedEnhanced());
    }

    public function testMultipleRegular()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEquals("working", $fixture->multipleRegular());
    }

    public function testMultipleEnhanced()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEquals("working", $fixture->multipleEnhanced());
    }

    public function testMixed()
    {
        $fixture = new Fixture\Fixture();

        $this->assertEquals("working", $fixture->mixed("foo"));
    }
}
