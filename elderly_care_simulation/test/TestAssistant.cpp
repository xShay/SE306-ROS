#include "Assistant.h"
#include <gtest/gtest.h>

TEST(DoubleEqualsTest, returnTrue)
{
    EXPECT_TRUE(doubleEquals(0.0, 0.0, 0.05));
    EXPECT_TRUE(doubleEquals(1.2, 1.2001, 0.03));
    EXPECT_TRUE(doubleEquals(2.2, 2.22, 0.03));
    EXPECT_TRUE(doubleEquals(3.5, 4.4, 1.0));
    EXPECT_TRUE(doubleEquals(3.14159, 3.14158, 0.00002));

    EXPECT_TRUE(doubleEquals(-0.0, -0.0, 0.05));
    EXPECT_TRUE(doubleEquals(-1.2, -1.2001, 0.03));
    EXPECT_TRUE(doubleEquals(-2.2, -2.22, 0.03));
    EXPECT_TRUE(doubleEquals(-3.5, -4.4, 1.0));
    EXPECT_TRUE(doubleEquals(-3.14159, -3.14158, 0.00002));
}

TEST(DoubleEqualsTest, returnFalse)
{
    EXPECT_FALSE(doubleEquals(-1.2, 1.2, 1));
    EXPECT_FALSE(doubleEquals(2.2, 2.02, 0.03));
    EXPECT_FALSE(doubleEquals(3.5, 4.4, 0.5));
    EXPECT_FALSE(doubleEquals(3.14159, 3.14158, 0));
}

// Run all the tests that were declared with TEST()
int main(int argc, char **argv){
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
