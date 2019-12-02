import scala.io.StdIn.readLine

object Main {
  def fuel(mass: Int):Int = {
    val f = mass / 3 -2 
    if (f < 0) 0 
    else f + fuel(f)
  }

  def main(args: Array[String]): Unit = {
    val f = Iterator
      .continually(readLine())
      .takeWhile(_ != null)
      .map(elem => fuel(elem.toInt)) 
      .sum
    println(f)
  }
}
