
import 'package:flutter/material.dart';
import 'package:flutter_app/exercise/exercise_form.dart';

class RoutinePage extends StatefulWidget {
  const RoutinePage({super.key});

  @override
  State<StatefulWidget> createState() => _RoutinePageState();
  
}

class _RoutinePageState extends State {
  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(),
    body: Padding(
      padding: EdgeInsetsGeometry.only(left: 40.0, right: 40.0),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            ExerciseForm(),
            ElevatedButton(
              child: const Icon(Icons.add),
              onPressed: () => {},
            ),
          ],
        ),
      ),
    ),
  );
  
}