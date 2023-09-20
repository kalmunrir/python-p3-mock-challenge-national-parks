class NationalPark:

    def __init__(self, name):
        self.name = name
        
    def __get_name(self):
        return self._name
    def __set_name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Name must be a string with length greater than or equal to 3")
    name = property(__get_name, __set_name)

    def trips(self):
        return ([trip for trip in Trip.all if trip.national_park == self])
    
    def visitors(self):
        visitors_to_park = []
        for trip in self.trips():
            if trip.visitor not in visitors_to_park:
                visitors_to_park.append(trip.visitor)
        return visitors_to_park
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitor_list = [trip.visitor for trip in self.trips()]
        best = -1
        for visitor in self.visitors():
            if visitor_list.count(visitor) > visitor_list.count(best):
                best = visitor
        return (best if visitor_list.count(best) != 0 else None)


class Trip:
    
    all = []

    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    DAYS = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def _get_start_date(self):
        return self._start_date
    def _set_start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7 and start_date.split(' ')[0] in self.MONTHS and start_date.split(' ')[1] in self.DAYS:
            self._start_date = start_date
        else:
            raise Exception('Invalid start_date')
    start_date = property(_get_start_date, _set_start_date)

    def _get_end_date(self):
        return self._end_date
    def _set_end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7 and end_date.split(' ')[0] in self.MONTHS and end_date.split(' ')[1] in self.DAYS:
            self._end_date = end_date
        else:
            raise Exception('Invalid end date')
    end_date = property(_get_end_date, _set_end_date)

    def _get_national_park(self):
        return self._national_park
    def _set_national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception('Invalid national park')
    national_park = property(_get_national_park, _set_national_park)


class Visitor:

    def __init__(self, name):
        self.name = name

    def __get_name(self):
        return self._name
    def __set_name(self, name):
        if isinstance(name, str) and len(name) >= 1 and len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string and between 1 and 15 characters in length")
    name = property(__get_name, __set_name)
        
    def trips(self):
        return ([trip for trip in Trip.all if trip.visitor == self])
    
    def national_parks(self):
        parks_visited = []
        for trip in self.trips():
            if trip.national_park not in parks_visited:
                parks_visited.append(trip.national_park)
        return parks_visited
    
    def total_visits_at_park(self, park):
        if isinstance(park, NationalPark):
            return self.trips().count(park)
        else:
            raise Exception("Must pass a NationalPark obj as an argument")